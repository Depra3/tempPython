-- 한 줄 주석
/* 
	여러 
	줄 
	주석 
*/

-- 관계형 데이터베이스
-- oracle, mysql, mssql

-- no sql
-- mongodb

-- db server > database > table > row, column

-- ctrl + enter 		- 선택된 한 줄 실행
-- ctrl + shift + enter - 전체 실행 or 블럭 실행(블럭 지정 - 드래그)

create database shopdb;

/*	char	- 메모리를 고정적으로 먹음
	varchar	- 메모리를 유동적으로 먹음(적게 들어오면 그것에 맞춰서 메모리 적용)
*/
create table membertbl
( 	memberid char(5) primary key, -- pk 중복값, null값 불허
	membername char(5),
    memberaddress char(15));
    
create table producttbl
(	productname varchar(10) primary key,
	cost int,
    makedate date,
    company char(5),
    amount int);

drop table membertbl;
insert into membertbl values('dang','당당이','경기도 부천시 중동');
insert into membertbl values('han','한국찬','인천시 남구 주안동');
insert into membertbl values('joe','지운이','서울시 은평구 중동');
insert into membertbl values('sung','상길이','경기도 분당구 서현동');

select * from membertbl;

drop table producttbl;
insert into producttbl values('냉장고', 5, '2019-03-03', '대우', 23);
insert into producttbl values('세탁기', 20, '2018-09-01', 'LG', 3);
insert into producttbl values('컴퓨터', 10, '2001-05-03', '삼성', 11);

select * from producttbl;

show tables;
use shopdb;		-- 어느 데이터 베이스를 사용할지 명시해야함 / 더블클릭으로 굵은 글씨를 만들어도 됨

-- select 선택 칼럼명... from 테이블명 where 조건;
select * from membertbl;
select * from producttbl;

-- 제조 일자가 2019년 이전에 제조된 제품을 출력
select * from producttbl where makedate < '2019-01-01';

-- 재고가 10미만인 제품의 이름을 출력
select productname from producttbl where amount < 10;

-- 아이디 han인 사람의 이름과 주소를 출력
select membername, memberaddress from membertbl where memberid = 'han';

-- 대우에서 생상된 제품의 이름을 출력
select productname from producttbl where company = '대우';

-- employees database에서 남성 사원의 정보를 모두 출력
-- select * from employees.employees where gender = 'M';
use employees;
select * from employees where gender = 'M';

-- 출생년도가 1960년 이전 출신의 정보 출력
select * from employees where birth_date < '1960-01-01';

-- 연봉이 10만 달러 이상인 사람들의 사번을 출력
select * from salaries;
select emp_no from salaries where salary >= 100000 group by emp_no;

-- 연봉이 10만 달러 이상인 사람들의 수를 출력
select count(*) from salaries where salary >= 100000;

-- shopdb에서 세탁기를 만든 회사 출력
select company from producttbl where productname = '세탁기';

-- 인천에 사는 사람의 이름 출력
select membername from membertbl where memberaddress like '%인천%';

-- 재고 총액이 100 미만인 제품을 출력
select * from producttbl where cost*amount < 100;

use sqldb;
show tables;
select * from buytbl;
select * from usertbl;
-- 김경호라는 가수의 데이터 출력
select * from usertbl where name = '김경호';

-- 출생년도가 1970년 이후이고, 키가 182이상인 회원 출력
select * from usertbl where birthYear>1970 && height>=182;

-- 출생년도가 1970년 이후이고, 키가 182이상인 회원의 아이디 출력
select userID from usertbl where birthYear>1970 && height>=182;

-- 출생년도가 1970년 이후이거나, 키가 182이상인 회원 출력
select * from usertbl where birthYear>1970 || height>=182;
-- 출생지가 '경남' 또는 '전남' 또는 '경북'인 회원의 이름과 주소 출력
select name, addr from usertbl where addr in ('경남', '전남', '경북');

-- 성이 '김'인 사람 출력
select * from usertbl where name like '김%';

-- '김경호'보다 키가 큰 사람의 데이터를 출력  - subquery
select * from usertbl where height>(select height from usertbl where name = '김경호');

-- '임재범' 보다 나이가 많은 사람의 데이터 출력 - subquery
select * from usertbl where birthYear<(select birthYear from usertbl where name = '임재범');

-- '경남'에 사는 사람보다 키가 큰 사람의 데이터 출력 
-- > 1. '경남'에 사는 모든 사람보다 키가 큰경우 or 2. '경남'에 사는 어떤 사람보다도 키가 큰 경우
-- subqurey를 사용하지만 subquery의 결과가 복수인 경우
-- 1
select * from usertbl where height>all(select height from usertbl where addr='경남');
-- 2
select * from usertbl where height>any(select height from usertbl where addr='경남');
-- '경남'에 사는 어떤 사람과 키가 같은 경우
select * from usertbl where height in (select height from usertbl where addr='경남');

-- 출생 날짜를 기준으로 오름차순 정렬 출력
select * from usertbl order by birthYear;
-- 출생 날짜를 기준으로 내림차순 정렬 출력
select * from usertbl order by birthYear desc;

-- 출생지의 중복없는 unique값들을 출력 - distinct
select addr from usertbl group by addr;
select distinct addr from usertbl;

-- 출생지의 종류는 몇가지 인가?
select count(distinct addr) from usertbl;

-- 출력 데이터의 수 제한 : limit
select * from usertbl limit 3;

-- usertbl에서 키가 가장 큰 사람의 데이터를 출력
select * from usertbl where height = (select max(height) from usertbl);

-- usertbl에서 키가 가장 큰사람과 작은 사람의 데이터를 출력
select * from usertbl 
where height in ((select max(height) from usertbl), (select min(height) from usertbl));

-- 사용자별 총 구매금액이 1000이상인 고객의 데이터 출력
select * from usertbl where userID in (select userID from buytbl where (price*amount)>=1000);
-- group by를 하는 경우 조건 having O - where X  / as 생략 가능
select userID, sum(price*amount) as tot_amount from buytbl
group by userID having sum(price*amount)>=1000;

-- 사용자별 총 구매횟수가 2회 이상인 고객의 정보 출력
select * from usertbl where userID in (select userID from buytbl group by userID having count(userID)>=2);

select first_name, last_name, email from customer where customer_id in (select customer_id from rental group by customer_id having count(customer_id)>=30);