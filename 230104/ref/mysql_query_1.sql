-- 한 줄 주석

/*
여러 줄 주석
여러 줄 주석
*/


-- 관계형 데이터베이스
-- oracle, mysql, mssql

-- no sql
-- mongodb

-- db server > database > table > row, column

-- ctrl + enter - 선택된 한 줄 실행
-- ctrl + shift + enter - 전체실행 or 블록실행

create database shopdb;

use shopdb;

create table membertbl
(memberid char(5) primary key,  -- 중복값 불허, null값 불허
membername char(5),
memberaddress char(15));

create table productbl
(productname varchar(10) primary key,
cost int,
makedate date,
company char(5),
amount int);

insert into membertbl values('dang', '당당이', '경기도 부천시 중동');
insert into membertbl values('han', '한국찬', '인천시 남구 주안동');
insert into membertbl values('joe', '지운이', '서울시 은평구 중동');
insert into membertbl values('sung', '상길이', '경기도 분당구 서현동');

select * from membertbl;

insert into productbl values('냉장고', 5, '2019-03-01', '대우', 23);
insert into productbl values('세탁기', 20, '2018-09-01', 'LG', 3);
insert into productbl values('컴퓨터', 10, '2001-05-03', '삼성', 11);

select * from productbl;

show tables;

select * from membertbl;
select * from productbl;

-- 제조 일자가 2019년 이전에 제조된 제품을 출력..
select * from productbl where makedate < '2019-01-01';

-- 재고가 10 미만인 제품의 이름을 출력..
select * from productbl where amount < 10;

-- 아이디 han인 사람의 이름과 주소를 출력..
select membername, memberaddress from membertbl where memberid = 'han';

-- 대우에서 생산된 제품의 이름을 출력하시오..
select productname from productbl where company='대우';


-- employees database에서 남성사원의 정보를 모두 출력...
use employees;

select * from employees where gender = 'M';

-- 출생년도가 1960년 이전 출신의 사원정보를 출력..
select * from employees where birth_date < '1960-01-01';

-- 연봉이 10만달러 이상인 사람들의 사번을 출력하시오..
select emp_no from salaries where salary >= 100000;


-- select 선택칼럼명..... from  테이블명  where  조건;


-- 연봉이 10만달러 이상인 사람들의 수를 출력하시오..
select count(emp_no) from salaries where salary >= 100000;


-- shopdb에서 세탁기를 만든 회사는
use shopdb;
select company from productbl where productname = '세탁기';

-- 인천에 사는 사람의 이름은
select membername from membertbl where memberaddress like '%인천%';

-- 재고 총액이 100 미만인 제품을 출력..
select * from productbl where cost*amount < 100;

use sqldb;
show tables;

select * from buytbl;
select * from usertbl;

-- 김경호라는 가수의 데이터를 출력..
select * from usertbl where name = '김경호';
-- 출생년도가 1970년 이후이고, 키가 182 이상인 회원을 출력..
select * from usertbl where birthyear > 1970 and height > 182;
-- 출생년도가 1970년 이후이고, 키가 182 이상인 회원의 아이디을 출력..
select userid from usertbl where birthyear > 1970 and height > 182;
-- 출생년도가 1970년 이후이거나, 키가 182 이상인 회원을 출력..
select userid from usertbl where birthyear > 1970 or height > 182;
-- 출생지가 '경남' 또는 '전남' 또는 '경북'인  회원의 이름과 주소를 출력..
select userid, addr from usertbl where addr = '경남' or 
addr = '전남' or addr = '서울';

select userid, addr from usertbl where addr in ('경남', '전남', '서울');

-- 성이 '김'인 사람의 데이터 출력..
select * from usertbl where name like '김%';

-- '김경호'보다 키가 큰 사람의 데이터를 출력.. - subquery문
select * from usertbl where height 
> (select height from usertbl where name='김경호');

-- '임재범' 보다 나이가 많은 사람의 데이터를 출력.. - subquery 사용
select * from usertbl where birthyear < 
(select birthyear from usertbl where name='임재범');

-- '경남'에 사는 사람보다 키가 큰 사람의 데이터를 출력.
-- subquery를 사용하지만 subquery의 결과가 복수인 경우..'
select * from usertbl where height 
> (select height from usertbl where addr = '경남');

-- 1) '경남'에 사는 모든 사람보다 키가 큰 경우
select * from usertbl where height 
> all(select height from usertbl where addr = '경남');

-- 2) '경남'에 사는 어떤 사람보다도 키가 크면 ok
select * from usertbl where height 
> any(select height from usertbl where addr = '경남');

-- 3) '경남'에 사는 어떤 사람과 키가 같으면 ok
select * from usertbl where height 
in (select height from usertbl where addr = '경남');

-- 출생 날짜를 기준으로 오름차순 정렬 출력..
select * from usertbl order by birthyear;

-- 출생 날짜를 기준으로 내림차순 정렬 출력..
select * from usertbl order by birthyear desc;

-- 출생지의 중복없는 unique값들을 출력하시오..
select distinct addr from usertbl;

-- 출생지의 종류는 몇 가지인가?
select count(distinct addr) from usertbl;

-- 출력데이터의 수 제한 : limit
select * from usertbl limit 5;


-- usertbl에서 키가 가장 큰 사람의 데이터를 출력..
select * from usertbl 
where height = (select max(height) from usertbl);

-- usertbl에서 키가 가장 큰 사람과 가장 작은 사람의 이름을 출력하시오..
select * from usertbl 
where height in ((select max(height) from usertbl), 
(select min(height) from usertbl));

-- 사용자별 총구매금액이 1000 이상인 고객의 데이터를 출력..

select userid, sum(price*amount) from buytbl 
group by userid 
having sum(price*amount) > 1000;
-- group by하는 경우 조건은 where가 아니라 having...

select userid, sum(price*amount) as tot_amount from buytbl 
group by userid 
having tot_amount > 1000;

-- 사용자별 총구매횟수가 2회 이상인 고객의 정보를 출력하시오..alter
select userid, count(userid) as buy_count from buytbl
group by userid
having buy_count > 2;


### sql 기본 함수 ###

-- cast : 













