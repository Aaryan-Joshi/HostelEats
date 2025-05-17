<?php
include 'connect.php';

// Get the form data
$name = $_POST['name'];
$room = $_POST['room'];
$food = $_POST['food'];
$address = $_POST['address'];
$hostel_name = $_POST['hostel_name'];
$phone_number = $_POST['phone_number'];

// Insert data into the 'orders' table
$sql = "INSERT INTO orders (name, room, food, address, hostel_name, phone_number) 
        VALUES ('$name', '$room', '$food', '$address', '$hostel_name', '$phone_number')";
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order Status | HostelEats</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<?php if ($conn->query($sql) === TRUE): ?>
    <div class="success-message">
        <h2>Order Placed Successfully!</h2>
        <a href="index.html" class="return-button">Return to Home</a>
    </div>
<?php else: ?>
    <div class="success-message">
        <h2>Error placing order!</h2>
        <p><?php echo $conn->error; ?></p>
        <a href="index.html" class="return-button">Return to Home</a>
    </div>
<?php endif; ?>

<?php $conn->close(); ?>

</body>
</html>
