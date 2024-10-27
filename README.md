## Dagster - dbt New York Taxi Trips Project  
In this project, I Orchestrated a dbt project using dagster.  
By loading and connecting the dbt project with dagster, each dbt model maps to an asset in dagster
I combined the assets from a previous [dagster project](https://github.com/Abdulshakur54/NY-Taxi-Trips-) with the ones from dbt project to make a robust pipeline [finished project in the dagster UI](https://drive.google.com/file/d/1uLf1xotQuXTHD21v-184-J_pPGD68RKf/view?usp=sharing).

**There are many benefits one gets from combining dagster with dbt. it includes but are not limited to the following**    
1. Orchestration of the dbt models   
2. dbt only performs the "T" in the "ELT" process. combining with Dagster, Dagster handles the "EL" in the "ELT" process  
3. Core dbt does not support ochestration, with dagster, You can ochestrate dbt jobs as pipelines
4. dbt increemental runs aren’t repeatable. combining with dbt helps us to repeat incremental runs using dagster partitions
5. dagster assets can be made an upstream for dbt models transformed assets and dbt assets can be used as upstream for dagster assets as well  
  
**The generated artifacts from the pipeline after analysing is shown below**
1. [airport trips chart](./data/outputs/airport_trips.png)
2. [manhattan map image](./data/outputs/manhattan_map.png)
3. [trips by week csv](./data//outputs/trips_by_week.csv)

## Deployment
This project on completion on my local machine (Dev environment) was hosted in [Dagster+](https://docs.dagster.io/dagster-plus), a cloud platform for production environment.  
I configured CI/CD pipeline from this github repository to Dagster+.
The materialization was tested in the production environment and it went smoothly.



