# k-hammer
This is a project to deploy and run the database benchmark tool hammerdb.  This
can be run in a kubernetes job or manually.
# deployment
To deploy:

    oc apply -f k8s/hammerdb

This will deploy the following pods:

    mariadb-ephemeral    - mariadb that is using the ephemeral disk for storage
    mariadb              - mariadb that is using a persistent volume for storage
    hammerdb             - can run the hammerdb manually
# To run in a kubernetes job
Just create the job with the yaml in the top directory of the repo.  Naming convention is

    job-<benchmark>-<database>[-<ephemeral>]

To run the tprocc benchmark on mariadb backed by a persistent volume:

    oc create -f job-tprocc-mariadb.yaml

To run the tprocc benchmark on mariadb backed by ephemeral storage

    oc create -f job-tprocc-mariadb-ephemeral.yaml	 

Creating the job will start a container to run the benchmark.  To find the correct
container, uss:

    oc get pods

with the correct container name, get the logs via

    oc logs <name from previous step>

Look for the line 
  
    TEST RESULT : System achieved 2278 NOPM from 5263 MariaDB TPM

To get the transactions per minute (TPM)
# To run manually
Running manually is done with the following steps:
    1) use oc login to the correct cluster and project
    2) rsh into the correct container:

        oc rsh hammerdb...
    
    3) Build the schema in the database with: 
    
        ./hammerdbcli auto maria_ephemeral_tprocc_build.tcl
    
    4) Run the benchmark with:
    
        ./hammerdbcli auto maria_ephemeral_tprocc_run.tcl
    
    5) look for the "TEST RESULT" line to get the results
# To modify the script
The scripts are located in the k8s/hammerdb/hammerdb-scripts subdirectory.
And there is a comment that lists most of the parameters that can be 
adjusted.

They are loaded with a configmap that is defined in the kustomization file.

