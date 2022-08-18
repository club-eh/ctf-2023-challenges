<?php
/*
 * Author:	Nemi Rai
 * Purpose:	Creates a connection to a database, searches it based off
 * 			form input, and prints the results.
 */

	function search(){
		// connect to database, change here if using another db
		$servername = "localhost";
		$username = "ctf";
		$password = "ctf";
		$dbname = "ctf";
		$conn = new mysqli($servername, $username, $password, $dbname);
		if ($conn->connect_error) {
			die("Connection failed: " . $conn->connect_error);
		}

		// get search term, create and execute query
		$term = $_REQUEST['search'];
		$sql = "SELECT * FROM one WHERE name LIKE '$term' OR description LIKE '% $term %'";
		$result = $conn->query($sql);

		// display results
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
