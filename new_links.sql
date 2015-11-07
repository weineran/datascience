----------------------------------------------------------------------------------------------
--SQL script to investigate new links for each month
--We say that a link is 'new' if it shows up in one month and did not show up in the prior month.
--We are aware that if a link shows up in January, then doesn't show up in February, then shows up again in
--   March, it will be counted as 'new' even though it was seen two months ago.
--
-- INSTRUCTIONS: This is a PostgreSQL query.  It might need minor editing for MySQL.
--               For PostgreSQL, just copy all the text into a query and execute it.
--               Total execution time should be 40-60 minutes (estimated based on me running
--               it in bits and pieces and keeping tracking of how long each one took).
----------------------------------------------------------------------------------------------


----------------------------------------------------------------------------------------------
--create tables for 'new' ipv4 and ipv6 links
-- TIME: approx 0
----------------------------------------------------------------------------------------------
CREATE TABLE new_ipv4_links
(
  new_links_uid serial PRIMARY KEY,
  link_name text,
  month_num integer
);

CREATE TABLE new_ipv6_links
(
  new_links_uid serial PRIMARY KEY,
  link_name text,
  month_num integer
);


----------------------------------------------------------------------------------------------
-- First we work on IPv4
----------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------
--create IPv4 tables by month
-- TIME: approx 0
----------------------------------------------------------------------------------------------
CREATE TABLE ipv4linksJan
(  
  link_name text PRIMARY KEY,
  month_num integer
);
CREATE TABLE ipv4linksFeb
(  
  link_name text PRIMARY KEY,
  month_num integer
);
CREATE TABLE ipv4linksMar
(  
  link_name text PRIMARY KEY,
  month_num integer
);
CREATE TABLE ipv4linksApr
(  
  link_name text PRIMARY KEY,
  month_num integer
);
CREATE TABLE ipv4linksMay
(  
  link_name text PRIMARY KEY,
  month_num integer
);
CREATE TABLE ipv4linksJun
(  
  link_name text PRIMARY KEY,
  month_num integer
);
CREATE TABLE ipv4linksJul
(  
  link_name text PRIMARY KEY,
  month_num integer
);
CREATE TABLE ipv4linksAug
(  
  link_name text PRIMARY KEY,
  month_num integer
);
CREATE TABLE ipv4linksSep
(  
  link_name text PRIMARY KEY,
  month_num integer
);
CREATE TABLE ipv4linksOct
(  
  link_name text PRIMARY KEY,
  month_num integer
);
CREATE TABLE ipv4linksNov
(  
  link_name text PRIMARY KEY,
  month_num integer
);
CREATE TABLE ipv4linksDec
(  
  link_name text PRIMARY KEY,
  month_num integer
);



----------------------------------------------------------------------------------------------
-- insert records into IPv4 monthly tables
-- TIME: approx 130 seconds per table * 12 tables = ~25-30 min
----------------------------------------------------------------------------------------------
INSERT INTO ipv4linksJan (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
1 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1388534400 AND as_links_direct.timestamp_latest < 1391212800 AND as_links_direct.ip_version='IPv4'
ORDER BY link_name;

INSERT INTO ipv4linksFeb (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
2 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1391212800 AND as_links_direct.timestamp_latest < 1393632000 AND as_links_direct.ip_version='IPv4'
ORDER BY link_name;

INSERT INTO ipv4linksMar (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
3 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1393632000 AND as_links_direct.timestamp_latest < 1396310400 AND as_links_direct.ip_version='IPv4'
ORDER BY link_name;

INSERT INTO ipv4linksApr (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
4 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1396310400 AND as_links_direct.timestamp_latest < 1398902400 AND as_links_direct.ip_version='IPv4'
ORDER BY link_name;

INSERT INTO ipv4linksMay (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
5 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1398902400 AND as_links_direct.timestamp_latest < 1401580800 AND as_links_direct.ip_version='IPv4'
ORDER BY link_name;

INSERT INTO ipv4linksJun (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
6 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1401580800 AND as_links_direct.timestamp_latest < 1404172800 AND as_links_direct.ip_version='IPv4'
ORDER BY link_name;

INSERT INTO ipv4linksJul (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
7 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1404172800 AND as_links_direct.timestamp_latest < 1406851200 AND as_links_direct.ip_version='IPv4'
ORDER BY link_name;

INSERT INTO ipv4linksAug (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
8 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1406851200 AND as_links_direct.timestamp_latest < 1409529600 AND as_links_direct.ip_version='IPv4'
ORDER BY link_name;

INSERT INTO ipv4linksSep (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
9 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1409529600 AND as_links_direct.timestamp_latest < 1412121600 AND as_links_direct.ip_version='IPv4'
ORDER BY link_name;

INSERT INTO ipv4linksOct (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
10 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1412121600 AND as_links_direct.timestamp_latest < 1414800000 AND as_links_direct.ip_version='IPv4'
ORDER BY link_name;

INSERT INTO ipv4linksNov (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
11 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1414800000 AND as_links_direct.timestamp_latest < 1417392000 AND as_links_direct.ip_version='IPv4'
ORDER BY link_name;

INSERT INTO ipv4linksDec (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
12 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1417392000 AND as_links_direct.timestamp_latest < 1420070400 AND as_links_direct.ip_version='IPv4'
ORDER BY link_name;


----------------------------------------------------------------------------------------------
-- Find links that are new for each month and insert into table new_ipv4_links
-- TIME: a few seconds
----------------------------------------------------------------------------------------------
INSERT INTO new_ipv4_links (link_name, month_num)
 SELECT link_name, month_num FROM ipv4linksFeb WHERE link_name NOT IN (SELECT link_name FROM ipv4linksJan);

INSERT INTO new_ipv4_links (link_name, month_num)
 SELECT link_name, month_num FROM ipv4linksMar WHERE link_name NOT IN (SELECT link_name FROM ipv4linksFeb);

INSERT INTO new_ipv4_links (link_name, month_num)
 SELECT link_name, month_num FROM ipv4linksApr WHERE link_name NOT IN (SELECT link_name FROM ipv4linksMar);

INSERT INTO new_ipv4_links (link_name, month_num)
 SELECT link_name, month_num FROM ipv4linksMay WHERE link_name NOT IN (SELECT link_name FROM ipv4linksApr);

INSERT INTO new_ipv4_links (link_name, month_num)
 SELECT link_name, month_num FROM ipv4linksJun WHERE link_name NOT IN (SELECT link_name FROM ipv4linksMay);

INSERT INTO new_ipv4_links (link_name, month_num)
 SELECT link_name, month_num FROM ipv4linksJul WHERE link_name NOT IN (SELECT link_name FROM ipv4linksJun);

INSERT INTO new_ipv4_links (link_name, month_num)
 SELECT link_name, month_num FROM ipv4linksAug WHERE link_name NOT IN (SELECT link_name FROM ipv4linksJul);

INSERT INTO new_ipv4_links (link_name, month_num)
 SELECT link_name, month_num FROM ipv4linksSep WHERE link_name NOT IN (SELECT link_name FROM ipv4linksAug);

INSERT INTO new_ipv4_links (link_name, month_num)
 SELECT link_name, month_num FROM ipv4linksOct WHERE link_name NOT IN (SELECT link_name FROM ipv4linksSep);

INSERT INTO new_ipv4_links (link_name, month_num)
 SELECT link_name, month_num FROM ipv4linksNov WHERE link_name NOT IN (SELECT link_name FROM ipv4linksOct);

INSERT INTO new_ipv4_links (link_name, month_num)
 SELECT link_name, month_num FROM ipv4linksDec WHERE link_name NOT IN (SELECT link_name FROM ipv4linksNov);



----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
-- below we work on IPv6 --
----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------


----------------------------------------------------------------------------------------------
--create IPv6 tables by month
-- TIME: approx 0
----------------------------------------------------------------------------------------------
CREATE TABLE ipv6linksJan
(  
  link_name text PRIMARY KEY,
  month_num integer
);
CREATE TABLE ipv6linksFeb
(  
  link_name text PRIMARY KEY,
  month_num integer
);
CREATE TABLE ipv6linksMar
(  
  link_name text PRIMARY KEY,
  month_num integer
);
CREATE TABLE ipv6linksApr
(  
  link_name text PRIMARY KEY,
  month_num integer
);
CREATE TABLE ipv6linksMay
(  
  link_name text PRIMARY KEY,
  month_num integer
);
CREATE TABLE ipv6linksJun
(  
  link_name text PRIMARY KEY,
  month_num integer
);
CREATE TABLE ipv6linksJul
(  
  link_name text PRIMARY KEY,
  month_num integer
);
CREATE TABLE ipv6linksAug
(  
  link_name text PRIMARY KEY,
  month_num integer
);
CREATE TABLE ipv6linksSep
(  
  link_name text PRIMARY KEY,
  month_num integer
);
CREATE TABLE ipv6linksOct
(  
  link_name text PRIMARY KEY,
  month_num integer
);
CREATE TABLE ipv6linksNov
(  
  link_name text PRIMARY KEY,
  month_num integer
);
CREATE TABLE ipv6linksDec
(  
  link_name text PRIMARY KEY,
  month_num integer
);

----------------------------------------------------------------------------------------------
-- insert records into IPv6 monthly tables
-- TIME: approx 10 minutes
----------------------------------------------------------------------------------------------
INSERT INTO ipv6linksJan (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
1 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1388534400 AND as_links_direct.timestamp_latest < 1391212800 AND as_links_direct.ip_version='IPv6'
ORDER BY link_name;

INSERT INTO ipv6linksFeb (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
2 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1391212800 AND as_links_direct.timestamp_latest < 1393632000 AND as_links_direct.ip_version='IPv6'
ORDER BY link_name;

INSERT INTO ipv6linksMar (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
3 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1393632000 AND as_links_direct.timestamp_latest < 1396310400 AND as_links_direct.ip_version='IPv6'
ORDER BY link_name;

INSERT INTO ipv6linksApr (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
4 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1396310400 AND as_links_direct.timestamp_latest < 1398902400 AND as_links_direct.ip_version='IPv6'
ORDER BY link_name;

INSERT INTO ipv6linksMay (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
5 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1398902400 AND as_links_direct.timestamp_latest < 1401580800 AND as_links_direct.ip_version='IPv6'
ORDER BY link_name;

INSERT INTO ipv6linksJun (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
6 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1401580800 AND as_links_direct.timestamp_latest < 1404172800 AND as_links_direct.ip_version='IPv6'
ORDER BY link_name;

INSERT INTO ipv6linksJul (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
7 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1404172800 AND as_links_direct.timestamp_latest < 1406851200 AND as_links_direct.ip_version='IPv6'
ORDER BY link_name;

INSERT INTO ipv6linksAug (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
8 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1406851200 AND as_links_direct.timestamp_latest < 1409529600 AND as_links_direct.ip_version='IPv6'
ORDER BY link_name;

INSERT INTO ipv6linksSep (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
9 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1409529600 AND as_links_direct.timestamp_latest < 1412121600 AND as_links_direct.ip_version='IPv6'
ORDER BY link_name;

INSERT INTO ipv6linksOct (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
10 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1412121600 AND as_links_direct.timestamp_latest < 1414800000 AND as_links_direct.ip_version='IPv6'
ORDER BY link_name;

INSERT INTO ipv6linksNov (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
11 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1414800000 AND as_links_direct.timestamp_latest < 1417392000 AND as_links_direct.ip_version='IPv6'
ORDER BY link_name;

INSERT INTO ipv6linksDec (link_name, month_num)
SELECT DISTINCT ON (link_name)
CONCAT(CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.from_as ELSE as_links_direct.to_as END, 
 '<->',
 CASE WHEN as_links_direct.from_as > as_links_direct.to_as THEN as_links_direct.to_as ELSE as_links_direct.from_as END) as link_name,
12 as month_num
from as_links_direct WHERE as_links_direct.timestamp_earliest>=1417392000 AND as_links_direct.timestamp_latest < 1420070400 AND as_links_direct.ip_version='IPv6'
ORDER BY link_name;

----------------------------------------------------------------------------------------------
-- Find links that are new for each month and insert into table new_ipv6_links
-- TIME: approx 0
----------------------------------------------------------------------------------------------
INSERT INTO new_ipv6_links (link_name, month_num)
 SELECT link_name, month_num FROM ipv6linksFeb WHERE link_name NOT IN (SELECT link_name FROM ipv6linksJan);

INSERT INTO new_ipv6_links (link_name, month_num)
 SELECT link_name, month_num FROM ipv6linksMar WHERE link_name NOT IN (SELECT link_name FROM ipv6linksFeb);

INSERT INTO new_ipv6_links (link_name, month_num)
 SELECT link_name, month_num FROM ipv6linksApr WHERE link_name NOT IN (SELECT link_name FROM ipv6linksMar);

INSERT INTO new_ipv6_links (link_name, month_num)
 SELECT link_name, month_num FROM ipv6linksMay WHERE link_name NOT IN (SELECT link_name FROM ipv6linksApr);

INSERT INTO new_ipv6_links (link_name, month_num)
 SELECT link_name, month_num FROM ipv6linksJun WHERE link_name NOT IN (SELECT link_name FROM ipv6linksMay);

INSERT INTO new_ipv6_links (link_name, month_num)
 SELECT link_name, month_num FROM ipv6linksJul WHERE link_name NOT IN (SELECT link_name FROM ipv6linksJun);

INSERT INTO new_ipv6_links (link_name, month_num)
 SELECT link_name, month_num FROM ipv6linksAug WHERE link_name NOT IN (SELECT link_name FROM ipv6linksJul);

INSERT INTO new_ipv6_links (link_name, month_num)
 SELECT link_name, month_num FROM ipv6linksSep WHERE link_name NOT IN (SELECT link_name FROM ipv6linksAug);

INSERT INTO new_ipv6_links (link_name, month_num)
 SELECT link_name, month_num FROM ipv6linksOct WHERE link_name NOT IN (SELECT link_name FROM ipv6linksSep);

INSERT INTO new_ipv6_links (link_name, month_num)
 SELECT link_name, month_num FROM ipv6linksNov WHERE link_name NOT IN (SELECT link_name FROM ipv6linksOct);

INSERT INTO new_ipv6_links (link_name, month_num)
 SELECT link_name, month_num FROM ipv6linksDec WHERE link_name NOT IN (SELECT link_name FROM ipv6linksNov);