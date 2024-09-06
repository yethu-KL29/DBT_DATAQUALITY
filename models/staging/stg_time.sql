-- models/staging/stg_time.sql
{{ config(schema='silver') }}

with source as (
  select * from {{ source('raw_data', 'DIM_TIME') }}
)

select
  time_id,
  date,
  day_of_week,
  month,
  quarter,
  year
from source

