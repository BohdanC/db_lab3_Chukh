CREATE TABLE channel (
	channel_id SERIAL,
	channel_title varchar(40) NOT NULL,
	PRIMARY KEY (channel_id)
);

CREATE TABLE category (
	category_id SERIAL,
	cat_name VARCHAR(50) NOT NULL,
	PRIMARY KEY (category_id)
);

CREATE TABLE country (
	country_id SERIAL,
	country_name VARCHAR(50) NOT NULL,
	PRIMARY KEY (country_id)
);

CREATE TABLE video (
	video_id SERIAL,
	title VARCHAR(100),
	views INT NOT NULL,
	channel_id INT NOT NULL,
	category_id INT NOT NULL,
	country_id INT NOT NULL,
	PRIMARY KEY (video_id),
	CONSTRAINT FK_channel
		FOREIGN KEY (channel_id)
			REFERENCES channel (channel_id) ON DELETE CASCADE,
	CONSTRAINT FK_category
		FOREIGN KEY (category_id)
	  		REFERENCES category (category_id) ON DELETE CASCADE,
	CONSTRAINT FK_country
		FOREIGN KEY (country_id)
	  		REFERENCES country (country_id) ON DELETE CASCADE
);
