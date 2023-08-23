CREATE TABLE `users` (
  `id` varchar(255) PRIMARY KEY NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `email` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `first_name` varchar(255),
  `last_name` varchar(255)
);

CREATE TABLE `books` (
  `id` varchar(255) PRIMARY KEY NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `ISBN` varchar(255) UNIQUE NOT NULL,
  `googlebooks_id` varchar(255) UNIQUE NOT NULL,
  `title` varchar(255),
  `description` text COMMENT 'short description about the book',
  `publisher` varchar(255),
  `publish_date` datetime
);

CREATE TABLE `readsessions` (
  `id` varchar(255) PRIMARY KEY NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `book_id` varchar(255) NOT NULL,
  `duration` int NOT NULL COMMENT 'Duration in terms of months'
);

CREATE TABLE `reviews` (
  `id` varchar(255) PRIMARY KEY NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `book_id` varchar(255) NOT NULL,
  `review` text NOT NULL
);

CREATE TABLE `shelfs` (
  `id` varchar(255) PRIMARY KEY NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `books_count` int,
  `name` varchar(255)
);

CREATE TABLE `shelfs_books` (
  `book_id` varchar(255) NOT NULL,
  `shelf_id` varchar(255) NOT NULL
);

CREATE TABLE `reports` (
  `id` varchar(255) PRIMARY KEY NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `report_month` varchar(255),
  `report_year` year,
  `duration` int NOT NULL COMMENT 'Duration in terms of month',
  `started_reading_count` int,
  `completed_reading_count` int,
  `completion_rate` int COMMENT 'in percentage'
);

CREATE TABLE `user_stats` (
  `id` varchar(255) PRIMARY KEY NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `user_id` varchar(255),
  `books_read` int,
  `speed` int,
  `reading_count` int,
  `completed_count` int
);

CREATE TABLE `trackers` (
  `id` varchar(255) PRIMARY KEY NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `duration` int NOT NULL COMMENT 'Duration in terms of month',
  `report_id` varchar(255) NOT NULL
);

ALTER TABLE `readsessions` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `readsessions` ADD FOREIGN KEY (`book_id`) REFERENCES `books` (`id`);

ALTER TABLE `reviews` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `reviews` ADD FOREIGN KEY (`book_id`) REFERENCES `books` (`id`);

ALTER TABLE `shelfs` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `shelfs_books` ADD FOREIGN KEY (`book_id`) REFERENCES `books` (`id`);

ALTER TABLE `shelfs_books` ADD FOREIGN KEY (`shelf_id`) REFERENCES `shelfs` (`id`);

ALTER TABLE `reports` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `user_stats` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `trackers` ADD FOREIGN KEY (`report_id`) REFERENCES `reports` (`id`);
