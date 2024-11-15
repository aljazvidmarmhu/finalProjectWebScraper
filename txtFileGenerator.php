<?php
// Database connection details
$databaseName = "finalProject";
$databaseTableName = "finalProjectTable";
$databasePassword = "finalProject2024!";
$databaseHost = "localhost";  // Change if needed
$databaseUser = "root";  // Your MySQL username

// Create a connection to the database
$connection = new mysqli($databaseHost, $databaseUser, $databasePassword, $databaseName);

// Check connection
if ($connection->connect_error) {
    die("Connection failed: " . $connection->connect_error);
}

// Query to select products
$query = "SELECT * FROM $databaseTableName";
$result = $connection->query($query);

// Initialize an array to hold products
$products = [];
if ($result->num_rows > 0) {
    // Fetch all products
    while ($row = $result->fetch_assoc()) {
        $products[] = $row;
    }
} else {
    echo "No products found.";
}

// Close the connection
$connection->close();

// Group products by store
$stores = [];
foreach ($products as $product) {
    $stores[$product['store']][] = $product;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Store Products</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            padding: 20px;
        }
        .store {
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            margin: 10px;
            padding: 15px;
            width: 25%;
        }
        h2 {
            text-align: center;
            color: #333;
        }
        .product {
            border-bottom: 1px solid #eee;
            padding: 10px 0;
            display: flex;
            align-items: center;
        }
        .product img {
            width: 100px;
            height: auto;
            margin-right: 10px;
        }
        .product h3 {
            margin: 0;
            font-size: 16px;
        }
        .product p {
            margin: 5px 0;
            color: #666;
        }
        .price {
            font-weight: bold;
            color: #d9534f;
        }
        /* Responsive Design */
        @media (max-width: 900px) {
            .store {
                width: 40%; /* Two columns on smaller screens */
            }
            
        }
        @media (max-width: 600px) {
            .store {
                width: 100%; /* Single column on very small screens */
            }
        }
    </style>
</head>
<body>

<div class="container">
    <?php foreach ($stores as $storeName => $products): ?>
        <div class="store">
            <h2><?php echo htmlspecialchars($storeName); ?></h2>
            <?php foreach ($products as $product): ?>
                <div class="product">
                    <img src="<?php echo htmlspecialchars($product['imageURL']); ?>" alt="<?php echo htmlspecialchars($product['productName']); ?>">
                    <div>
                        <h3><?php echo htmlspecialchars($product['productName']); ?></h3>
                        <p class="price"><?php echo htmlspecialchars($product['price']); ?></p>
                    </div>
                </div>
            <?php endforeach; ?>
        </div>
    <?php endforeach; ?>
</div>

</body>
</html>