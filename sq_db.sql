CREATE TABLE IF NOT EXISTS products (
id integer primary key autoincrement,
name text NOT NULL,
bottle_type text NOT NULL,
description text NOT NULL,
quick_describe text NOT NULL,
weight text NOT NULL,
amount text NOT NULL,
price text NOT NULL,
left_goods text NOT NULL,
url text NOT NULL,
image_url text NOT NULL,
time integer NOT NULL
);