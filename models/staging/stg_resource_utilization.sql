-- models/staging/stg_resource_utilisation.sql
{{ config(schema='silver') }}

with source as (
  select * from {{ source('raw_data', 'FACT_RESOURCE_UTILIZATION') }}
)

select
  resource_utilization_id,
  time_id,
  employee_id,
  project_id,
  department_id,
  utilization_hours,
  utilization_percentage,
  active
from source
