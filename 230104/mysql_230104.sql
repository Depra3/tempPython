# sql 기본 함수 #

-- cast : 데이터 타입변환
select cast('2020-10-19 12:35:12' as date) as 'Date';
select cast('2020-10-19 12:35:12' as Time) as 'Date';
select cast('2020-10-19 12:35:12' as datetime) as 'Date';

-- concat : 문자열을 이어주는 함수
select concat('100','원');

use sqldb;
select * from buytbl;
select * from usertbl;

select num, concat(cast(price as char(10)), ' x ', cast(amount as char(10)), ' = ') 
	as '가격*구매액', price*amount as '총 구매액' from buytbl;

-- concat_ws : 문자열을 이을 때 구분자를 넣는다.    
select concat_ws('/', '2000', '01', '20') as '날짜';

-- ifnull(p1,p2) : p1이 null이면 p2출력, p1이 null이 아니면 p1출력
select ifnull(null, 100);
select ifnull(10, 100);

-- insert('문자열1', index(시작위치), length(자리수), '문자열2') 
-- : 문자열1의 index위치에 문자열2를 length길이 만큼 삽입.
select insert('abcdefghi', 3, 4, '@@@@');
select insert('abcdefghi', 3, 2, '@@@@');

-- left('문자열', num) : 문자열 왼쪽 num 만큼 리턴
-- right('문자열', num) : 문자열 오른쪽 num 만큼 리턴
select left('abcdefghi', 3);
select right('abcdefghi', 3);

-- repeat('문자열', num) : 문자열을 num 만큼 반복
select repeat('abc', 100);

-- lower() : 소문자 변환 / upper() : 대문자 변환
select lower('ABC');
select upper('abc');

-- lpad('문자열1', num, '문자열2') : 문자열1을 num만큼 자리수를 늘리고 left에 문자열2로 채운다
select lpad('abc', 7, '@');
-- rpad('문자열1', num, '문자열2') : 문자열1을 num만큼 자리수를 늘리고 right에 문자열2로 채운다
select rpad('abc', 7, '@');

-- ltrim, rtirm : 왼쪽, 오른쪽 공백 제거
select ltrim('   abc   ');
select rtrim('   abc   ');

-- replace('문자열1', '문자열2', '문자열3') : 문자열1에서 문자열2를 문자열3으로 교체
select replace('hello world', 'hello', 'python');

-- space(num) : num만큼의 space를 얻는다.
select concat('hello', space(20), 'python');

-- abs() : 절대값을 리턴
select abs(-20);

-- ceiling : 올림 / floor() : 버림 / round() : 반올림
select ceiling(4.3);
select floor(4.9);
select round(4.2);
select round(4.6);

-- mod : 나머지
select mod(157, 10);

-- pow(p1, p2) : p1의 p2승
select pow(2,3);
-- sqrt(p1) : 루트 p1
select sqrt(9);

-- length() : byte 크기를 반환
select length('abc'); -- 1byte
select length('가나다'); -- 3byte

# mysql datatype 유형

## 문자형
-- char(num) : 고정길이 문자열 타입, 최대 글자수 : 1 ~ 255
-- varchar(num) : 가변길이 문자열 타입 - 메모리 절약, 속도가 느림, 최대 글자수 : 1 ~65535
-- Text : 65535의 텍스트를 저장
-- longtext : 최대 4MB의 텍스트를 저장

## 숫자형
-- int : 정수, -2147483648 ~ 2147483647
-- float : 실수형, -3.102823466e+38 ~ 1.175494351e-38

## 날짜형
-- date : yyyy-mm-dd('1001-01-01' ~ '9999-12-31')
-- time
-- datetime
-- year

use sqldb;
create table maxtable(col1 longtext, col2 longtext);

insert into maxtable values(repeat('a', 1000000), repeat('가', 1000000));
select * from maxtable;

## 데이터 저장용량 변경시(my.ini) 재시작
insert into maxtable values(repeat('a', 10000000), repeat('가', 10000000));