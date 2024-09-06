-- models/staging/stg_employee.sql
{{ config(schema='silver') }}

with source as (
  select * from {{ source('raw_data', 'DIM_EMPLOYEE') }}
)

select
  employee_id,
  employee_name,
  job_title,
  hire_date,
  department_id,
  location
from source
