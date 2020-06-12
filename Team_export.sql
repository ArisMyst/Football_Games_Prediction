--------------------------------------------------------
--  File created - Παρασκευή-Ιουνίου-12-2020   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table FTB_EN_PREMIERLEAGUE_VALUES
--------------------------------------------------------

  CREATE TABLE "SYSTEM"."FTB_EN_PREMIERLEAGUE_VALUES" 
   (	"ID" NUMBER, 
	"TEAM_NAME" VARCHAR2(50 BYTE), 
	"TEAM_VALUE" NUMBER, 
	"SQUAD_SIZE" NUMBER, 
	"AVG_VALUE" NUMBER, 
	"AVG_AGE" FLOAT(126), 
	"START_DATE" DATE, 
	"END_DATE" DATE, 
	"TEST" NUMBER(*,0)
   ) PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "SYSTEM" ;
REM INSERTING into SYSTEM.FTB_EN_PREMIERLEAGUE_VALUES
SET DEFINE OFF;
Insert into SYSTEM.FTB_EN_PREMIERLEAGUE_VALUES (ID,TEAM_NAME,TEAM_VALUE,SQUAD_SIZE,AVG_VALUE,AVG_AGE,START_DATE,END_DATE,TEST) values ('1','Man City','1300000000','25','52190000','27,4',to_date('01/08/19','DD/MM/RR'),to_date('31/01/20','DD/MM/RR'),null);
Insert into SYSTEM.FTB_EN_PREMIERLEAGUE_VALUES (ID,TEAM_NAME,TEAM_VALUE,SQUAD_SIZE,AVG_VALUE,AVG_AGE,START_DATE,END_DATE,TEST) values ('2','Liverpool','1190000000','24','46660000','27,9',to_date('01/08/19','DD/MM/RR'),to_date('01/08/20','DD/MM/RR'),null);
Insert into SYSTEM.FTB_EN_PREMIERLEAGUE_VALUES (ID,TEAM_NAME,TEAM_VALUE,SQUAD_SIZE,AVG_VALUE,AVG_AGE,START_DATE,END_DATE,TEST) values ('3','Tottenham','977000000','27','36190000','26,4',to_date('01/08/19','DD/MM/RR'),to_date('31/01/20','DD/MM/RR'),null);
Insert into SYSTEM.FTB_EN_PREMIERLEAGUE_VALUES (ID,TEAM_NAME,TEAM_VALUE,SQUAD_SIZE,AVG_VALUE,AVG_AGE,START_DATE,END_DATE,TEST) values ('4','Chelsea','844250000','26','32470000','26,3',to_date('01/08/19','DD/MM/RR'),to_date('31/01/20','DD/MM/RR'),null);
Insert into SYSTEM.FTB_EN_PREMIERLEAGUE_VALUES (ID,TEAM_NAME,TEAM_VALUE,SQUAD_SIZE,AVG_VALUE,AVG_AGE,START_DATE,END_DATE,TEST) values ('5','Man United','744250000','25','29770000','25,8',to_date('01/08/19','DD/MM/RR'),to_date('31/01/20','DD/MM/RR'),null);
Insert into SYSTEM.FTB_EN_PREMIERLEAGUE_VALUES (ID,TEAM_NAME,TEAM_VALUE,SQUAD_SIZE,AVG_VALUE,AVG_AGE,START_DATE,END_DATE,TEST) values ('6','Arsenal','682750000','25','27310000','25,1',to_date('01/08/19','DD/MM/RR'),to_date('31/01/20','DD/MM/RR'),null);
Insert into SYSTEM.FTB_EN_PREMIERLEAGUE_VALUES (ID,TEAM_NAME,TEAM_VALUE,SQUAD_SIZE,AVG_VALUE,AVG_AGE,START_DATE,END_DATE,TEST) values ('7','Leicester','505250000','26','19430000','26,7',to_date('01/08/19','DD/MM/RR'),to_date('31/01/20','DD/MM/RR'),null);
Insert into SYSTEM.FTB_EN_PREMIERLEAGUE_VALUES (ID,TEAM_NAME,TEAM_VALUE,SQUAD_SIZE,AVG_VALUE,AVG_AGE,START_DATE,END_DATE,TEST) values ('8','Everton','480700000','25','19230000','27,3',to_date('01/08/19','DD/MM/RR'),to_date('31/01/20','DD/MM/RR'),null);
Insert into SYSTEM.FTB_EN_PREMIERLEAGUE_VALUES (ID,TEAM_NAME,TEAM_VALUE,SQUAD_SIZE,AVG_VALUE,AVG_AGE,START_DATE,END_DATE,TEST) values ('9','Bournemouth','343750000','30','11460000','26',to_date('01/08/19','DD/MM/RR'),to_date('31/01/20','DD/MM/RR'),null);
Insert into SYSTEM.FTB_EN_PREMIERLEAGUE_VALUES (ID,TEAM_NAME,TEAM_VALUE,SQUAD_SIZE,AVG_VALUE,AVG_AGE,START_DATE,END_DATE,TEST) values ('10','West Ham','338750000','24','14110000','28,7',to_date('01/08/19','DD/MM/RR'),to_date('31/01/20','DD/MM/RR'),null);
Insert into SYSTEM.FTB_EN_PREMIERLEAGUE_VALUES (ID,TEAM_NAME,TEAM_VALUE,SQUAD_SIZE,AVG_VALUE,AVG_AGE,START_DATE,END_DATE,TEST) values ('11','Wolves','330800000','26','12720000','25,4',to_date('01/08/19','DD/MM/RR'),to_date('31/01/20','DD/MM/RR'),null);
Insert into SYSTEM.FTB_EN_PREMIERLEAGUE_VALUES (ID,TEAM_NAME,TEAM_VALUE,SQUAD_SIZE,AVG_VALUE,AVG_AGE,START_DATE,END_DATE,TEST) values ('12','Newcastle','293830000','32','9180000','27,3',to_date('01/08/19','DD/MM/RR'),to_date('31/01/20','DD/MM/RR'),null);
Insert into SYSTEM.FTB_EN_PREMIERLEAGUE_VALUES (ID,TEAM_NAME,TEAM_VALUE,SQUAD_SIZE,AVG_VALUE,AVG_AGE,START_DATE,END_DATE,TEST) values ('13','Aston Villa','261900000','27','9700000','27',to_date('01/08/19','DD/MM/RR'),to_date('31/01/20','DD/MM/RR'),null);
Insert into SYSTEM.FTB_EN_PREMIERLEAGUE_VALUES (ID,TEAM_NAME,TEAM_VALUE,SQUAD_SIZE,AVG_VALUE,AVG_AGE,START_DATE,END_DATE,TEST) values ('14','Watford','234000000','31','7550000','27,6',to_date('01/08/19','DD/MM/RR'),to_date('31/01/20','DD/MM/RR'),null);
Insert into SYSTEM.FTB_EN_PREMIERLEAGUE_VALUES (ID,TEAM_NAME,TEAM_VALUE,SQUAD_SIZE,AVG_VALUE,AVG_AGE,START_DATE,END_DATE,TEST) values ('15','Crystal Palace','232800000','25','9310000','28,8',to_date('01/08/19','DD/MM/RR'),to_date('31/01/20','DD/MM/RR'),null);
Insert into SYSTEM.FTB_EN_PREMIERLEAGUE_VALUES (ID,TEAM_NAME,TEAM_VALUE,SQUAD_SIZE,AVG_VALUE,AVG_AGE,START_DATE,END_DATE,TEST) values ('16','Southampton','227000000','23','9870000','25,9',to_date('01/08/19','DD/MM/RR'),to_date('31/01/20','DD/MM/RR'),null);
Insert into SYSTEM.FTB_EN_PREMIERLEAGUE_VALUES (ID,TEAM_NAME,TEAM_VALUE,SQUAD_SIZE,AVG_VALUE,AVG_AGE,START_DATE,END_DATE,TEST) values ('17','Brighton','214750000','26','8260000','27,8',to_date('01/08/19','DD/MM/RR'),to_date('31/01/20','DD/MM/RR'),null);
Insert into SYSTEM.FTB_EN_PREMIERLEAGUE_VALUES (ID,TEAM_NAME,TEAM_VALUE,SQUAD_SIZE,AVG_VALUE,AVG_AGE,START_DATE,END_DATE,TEST) values ('18','Burnley','192750000','24','8030000','29,1',to_date('01/08/19','DD/MM/RR'),to_date('31/01/20','DD/MM/RR'),null);
Insert into SYSTEM.FTB_EN_PREMIERLEAGUE_VALUES (ID,TEAM_NAME,TEAM_VALUE,SQUAD_SIZE,AVG_VALUE,AVG_AGE,START_DATE,END_DATE,TEST) values ('19','Norwich','152350000','24','6350000','27,6',to_date('01/08/19','DD/MM/RR'),to_date('31/01/20','DD/MM/RR'),null);
Insert into SYSTEM.FTB_EN_PREMIERLEAGUE_VALUES (ID,TEAM_NAME,TEAM_VALUE,SQUAD_SIZE,AVG_VALUE,AVG_AGE,START_DATE,END_DATE,TEST) values ('20','Sheffield United','119200000','28','4260000','28,3',to_date('01/08/19','DD/MM/RR'),to_date('31/01/20','DD/MM/RR'),null);
--------------------------------------------------------
--  Constraints for Table FTB_EN_PREMIERLEAGUE_VALUES
--------------------------------------------------------

  ALTER TABLE "SYSTEM"."FTB_EN_PREMIERLEAGUE_VALUES" MODIFY ("ID" NOT NULL ENABLE);