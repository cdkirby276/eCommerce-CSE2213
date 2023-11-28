CREATE TABLE 'cart' (
    'UserID' varchar(14) NOT NULL,
    'ISBN' varchar(13) NOT NULL,
    'Quantity' int(2) DEFAULT NULL
);

INSERT INTO cart (UserID, ISBN, Quantity)
VALUES ('999', '9780061120084', 1);

INSERT INTO cart (UserID, ISBN, Quantity)
VALUES ('999', '9781400079020', 1);

INSERT INTO cart (UserID, ISBN, Quantity)
VALUES ('999', '9780743273565', 1);

INSERT INTO cart (UserID, ISBN, Quantity)
VALUES ('775', '9780547928227', 1);

INSERT INTO cart (UserID, ISBN, Quantity)
VALUES ('775', '9780140449334', 1); 