CREATE TABLE IF NOT EXISTS requests(
  request_id integer primary key,
  type text,
  name text,
  date text);

CREATE TABLE IF NOT EXISTS comments(
  comment_id integer primary key,
  request_id integer,
  content text,
  date integer,
  foreign key (request_id) references requests(request_id) on delete cascade);
