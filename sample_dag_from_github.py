# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""DAG running in response to a Cloud Storage bucket change."""
from datetime import datetime
from datetime import timedelta

from airflow import models
from airflow.operators import bash_operator

default_args = {
    'owner': 'Example DAG from github',
    'start_date': datetime.now(),
    'depends_on_past': False,
    'email': [''],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Not scheduled, trigger only
with models.DAG(
    'Sample_DAG_Deployed_From_Github', default_args=default_args, schedule_interval=None) as dag:

  # Prints the dag_run's configuration, which includes information about the
  # Cloud Storage object change.
  print_gcs_info = bash_operator.BashOperator(
      task_id='print_gcs_info', bash_command='echo Hello')