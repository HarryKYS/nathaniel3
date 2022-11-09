RENAME TABLE topic TO topic_backup; --토픽테이블을 백업 테이블로 바군다
SELECT * FROM topic LEFT JOIN author ON topic.author_id = author.id;
SELECT topic.id AS topic_id,title,description,created,name,profile   FROM topic LEFT JOIN author ON topic.author_id = author.id;
-- topic.id AT topic_id  토픽테이블에 idFMF Topic_id로 변경해서 인식한다

modeling 검색해보기 테이블 만들때
데이터 백업하기 