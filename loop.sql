--select * from category

DO $$
DECLARE
    category_id  category.category_id%TYPE;
    cat_name     category.cat_name%TYPE;

BEGIN
    category_id := 10;
    cat_name := 'CategoryName';
    FOR counter IN 1..10
        LOOP
            INSERT INTO category(category_id, cat_name)
            VALUES (category_id + counter, cat_name || counter);
        END LOOP;
END;
$$
