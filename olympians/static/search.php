<?php
	/*
	 * Purpose:	MySQL search function that connects to a database, searches a term
	 * 		requested from HTML, and prints the results.
	 * 		
	 */
	function search(){
		// Credentials etc used in mysql connection and query
		$servername = "mysql";
		$username = "root";
		$password = "QTzp47dI5GoNqPzl";
		$dbname = "ctf";
		$table = "olympians";

		// Connect to database
		$conn = new mysqli($servername, $username, $password, $dbname);
		if ($conn->connect_error) {
			die("Connection failed: " . $conn->connect_error);
		}

		// Get search term, create and execute query
		$term = $_REQUEST['search'];
		$sql = "SELECT * FROM $table WHERE name LIKE '$term' OR description LIKE '% $term %'";
		$result = $conn->query($sql);

		// Display results as HTML
		echo "<hr>Search Query: $term<br>";
		echo "Results: $result->num_rows<br><hr>";
		if ($result->num_rows > 0) {
			while($row = $result->fetch_assoc()) {
				echo "Name: " . $row["name"] . "</br>";
				echo "Description: " . $row["description"] . "</br>";
			}
		}
		$conn->close();
	}
?>
