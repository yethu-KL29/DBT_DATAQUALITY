-- models/staging/stg_project.sql
{{ config(schema='silver') }}

with source as (
  select * from {{ source('raw_data', 'DIM_PROJECT') }}
)

select
  project_id,
  project_name,
  start_date,
  end_date,
  project_manager_id,
  budget
from source

