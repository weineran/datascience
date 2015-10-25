--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: as_link_direct_monitor_junction; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE as_link_direct_monitor_junction (
    asldm_uid integer,
    asld integer,
    monitor_ip text
);


ALTER TABLE as_link_direct_monitor_junction OWNER TO postgres;

--
-- Name: as_link_indirect_monitor_junction; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE as_link_indirect_monitor_junction (
    aslim_uid integer,
    asli integer,
    monitor text
);


ALTER TABLE as_link_indirect_monitor_junction OWNER TO postgres;

--
-- Name: as_links_direct; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE as_links_direct (
    asld_uid integer,
    ip_version text,
    time_period integer,
    timestamp_earliest integer,
    timestamp_latest integer,
    from_as text,
    to_as text
);


ALTER TABLE as_links_direct OWNER TO postgres;

--
-- Name: as_links_indirect; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE as_links_indirect (
    asli_uid integer,
    ip_version text,
    time_period integer,
    timestamp_earliest integer,
    timestamp_latest integer,
    from_as text,
    to_as text,
    gap_length integer
);


ALTER TABLE as_links_indirect OWNER TO postgres;

--
-- Name: autonomous_systems; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE autonomous_systems (
    as_number text
);


ALTER TABLE autonomous_systems OWNER TO postgres;

--
-- Name: monitor_time_period_junction; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE monitor_time_period_junction (
    mtp_uid integer,
    monitor text,
    time_period integer,
    monitor_key integer
);


ALTER TABLE monitor_time_period_junction OWNER TO postgres;

--
-- Name: monitors; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE monitors (
    monitor_ip text,
    ip_version text,
    autonomous_system text
);


ALTER TABLE monitors OWNER TO postgres;

--
-- Name: time_periods; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE time_periods (
    timeperiod_uid integer,
    timestamp_earliest integer,
    timestamp_latest integer
);


ALTER TABLE time_periods OWNER TO postgres;

--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

