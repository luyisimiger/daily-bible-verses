
UPDATE bible_verses SET text = text_rtf

-- remove \cf6
UPDATE bible_verses SET text = REPLACE( REPLACE(text, "{\cf6 ", "") , "}", "")
WHERE text LIKE '{\cf6 %}';

-- remove \i
UPDATE bible_verses SET text = REPLACE( REPLACE(text, "{\i ", "") , "}", "")
WHERE text LIKE '{\i %}';

-- remove \par
UPDATE bible_verses SET text = REPLACE(text, "\par ", "")
WHERE text LIKE '%\par %';


-- SELECT * FROM bible_verses WHERE text LIKE '%\par %';