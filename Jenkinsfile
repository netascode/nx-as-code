pipeline {
    agent any
    environment {
        CREDENTIALS = credentials('nexus_credentials')
    }
    stages {
        stage('Validate') {
            steps {
                sh 'ansible-playbook -i inventory/ nexus_validate.yaml'
            }
        }
        stage('Prepare') {
            steps {
                sh 'ansible-playbook -i inventory/ nexus_prepare.yaml -e "username=$CREDENTIALS_USR password=$CREDENTIALS_PSW"'
            }
        }
        stage('Deploy') {
            steps {
                sh 'ansible-playbook -i inventory/ nexus_deploy.yaml -e "username=$CREDENTIALS_USR password=$CREDENTIALS_PSW"'
            }
        }
        stage('Test') {
            steps {
                sh 'ansible-playbook -i inventory/ nexus_test.yaml -e "username=$CREDENTIALS_USR password=$CREDENTIALS_PSW"'
            }
        }  
            
    }
    post {
        always {
            junit 'test_results/nexus_*.xml'
            archiveArtifacts 'test_results/nexus_*.html'
        }
    }
}
