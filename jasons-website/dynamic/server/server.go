package main

import (
	"errors"
	"math/rand"
	"os"
	"time"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/template/handlebars"
	"github.com/golang-jwt/jwt/v4"
	"github.com/joho/godotenv"
	"golang.org/x/crypto/bcrypt"
)

// Route declarations.
const (
	routeLogin = "/login"
	routeHome  = "/"
)

// File containing the flag.
const (
	flagFile = "/flag.txt"
)

// Credentials for the user.
var (
	username     = "jason"
	passwordHash = []byte("$2a$10$NqtIPVwjrKmFOW4rUAMZqecVhlLr8WqYeSb.3xHS7iNkbYOy3tpoS")
)

// Environment variables mapping.
var (
	port   string
	secret string
)

// Error declarations.
var (
	errVariableDoesnotExist = errors.New("variable doesn't exist")
	errInvalidRequestBody   = errors.New("invalid request body")
	errInvalidCredentials   = errors.New("invalid credentials")
	errInternalServerError  = errors.New("internal server error")
)

func init() {
	// Load environment variables.
	godotenv.Load()

	var err error
	port, err = getEnvVariable("PORT")
	if err != nil {
		panic(err)
	}

	secret, err = getEnvVariable("SECRET")
	if err != nil {
		panic(err)
	}
}

// run registers the route handlers and starts the server.
func run() {
	templateEngine := handlebars.New("./views", ".html")
	app := fiber.New(fiber.Config{
		Views: templateEngine,
	})

	app.Static("/assets", "./assets", fiber.Static{
		Compress: true, // cache compressed files in-memory
	})

	app.Get("/", home)

	app.Get("/login", func(ctx *fiber.Ctx) error {
		tokenString := ctx.Cookies("token")
		if len(tokenString) != 0 {
			return ctx.Redirect(routeHome)
		}

		return ctx.Render("login", fiber.Map{}, "layouts/main")
	})

	app.Post("/login", login)

	app.Listen(port)
}

// getEnvVariable gets the environment variable with the given name.
func getEnvVariable(variableName string) (string, error) {
	variable := os.Getenv(variableName)

	if len(variable) == 0 {
		return "", errVariableDoesnotExist
	}

	return variable, nil
}

// home defines the route handler for index route.
func home(ctx *fiber.Ctx) error {
	tokenString := ctx.Cookies("token")
	if len(tokenString) == 0 {
		return ctx.Redirect(routeLogin)
	}

	// Parse the json web token.
	token, err := parseToken(tokenString)
	if err != nil {
		removeToken(ctx)
		return ctx.Redirect(routeLogin)
	}

	if !token.IsAdmin {
		return ctx.Redirect(routeLogin)
	}

	// Read flag file.
	flag, err := os.ReadFile(flagFile)
	if err != nil {
		ctx.Status(fiber.StatusInternalServerError)
		return errInternalServerError
	}

	return ctx.Render("home", fiber.Map{
		"flag": string(flag),
	}, "layouts/main")
}

// loginRequestBody is used to parse the request body for the post login route.
type loginRequestBody struct {
	Username string `json:"username"`
	Password string `json:"password"`
}

// login defines the route handler for the post login route.
func login(ctx *fiber.Ctx) error {
	requestBody := &loginRequestBody{}
	responseBody := fiber.Map{}

	if err := ctx.BodyParser(requestBody); err != nil {
		responseBody["error"] = errInvalidRequestBody.Error()
	}

	// Validate credentials.
	if requestBody.Username != username {
		responseBody["error"] = errInvalidCredentials.Error()
	}

	if err := bcrypt.CompareHashAndPassword(passwordHash, []byte(requestBody.Password)); err != nil {
		responseBody["error"] = errInvalidCredentials.Error()
	}

	// Check for custom headers.
	checkHeaders(ctx, responseBody)

	// Create authorization token.
	token, err := createToken()
	if err != nil {
		return err
	}

	ctx.Cookie(&fiber.Cookie{
		Name:     "token",
		Value:    token,
		HTTPOnly: true,
	})

	return ctx.JSON(responseBody)
}

// checkHeaders reads various custom request headers, appends to the response body
// based on that.
func checkHeaders(ctx *fiber.Ctx, response fiber.Map) {
	headers := ctx.GetReqHeaders()

	if random, ok := headers["X-Random"]; ok {
		response[random] = rand.Int31()
	} else if repeat, ok := headers["X-Repeat"]; ok {
		response[repeat] = repeat
	} else if env, ok := headers["X-Env"]; ok {
		response[env] = os.Getenv(env)
	}
}

// tokenClaims maps the json web token.
type tokenClaims struct {
	jwt.RegisteredClaims

	IsAdmin bool `json:"isAdmin"`
}

// createToken creates a new json web token for the user authentication.
func createToken() (string, error) {
	claims := &tokenClaims{
		RegisteredClaims: jwt.RegisteredClaims{
			IssuedAt: &jwt.NumericDate{
				Time: time.Now(),
			},
			ExpiresAt: &jwt.NumericDate{
				Time: time.Now().Add(time.Hour * 24),
			},
		},

		IsAdmin: true,
	}

	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)

	tokenValue, err := token.SignedString([]byte(secret))
	if err != nil {
		return "", err
	}

	return tokenValue, nil
}

// parseToken parses the token string into the register custom struct mappings.
func parseToken(token string) (*tokenClaims, error) {
	claims := &tokenClaims{}

	_, err := jwt.ParseWithClaims(
		token,
		claims,
		func(token *jwt.Token) (interface{}, error) {
			return []byte(secret), nil
		},
	)

	return claims, err
}

// removeToken removes the token cookie.
func removeToken(ctx *fiber.Ctx) {
	ctx.Cookie(&fiber.Cookie{
		Name:     "token",
		Value:    "",
		Expires:  time.Now().Add(time.Second * -1),
		HTTPOnly: true,
	})
}
