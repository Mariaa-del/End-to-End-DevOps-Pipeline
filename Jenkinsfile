def run(String cmd) {
    if (isUnix()) { sh cmd } else { bat cmd }
}
def runQuiet(String cmd) {
    if (isUnix()) { sh(script: cmd, returnStatus: true) } else { bat(script: cmd, returnStatus: true) }
}
def py() { return isUnix() ? 'python3' : 'python' }

pipeline {
    agent any
    environment {
        PATH = "C:\\Program Files\\Docker\\Docker\\resources\\bin;${env.PATH}"
    }
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Build') {
            steps { script { run("${py()} -m py_compile app.py") } }
        }
        stage('Test') {
            steps { script { run("${py()} -m unittest -v test_app.py") } }
        }
        stage('Docker Build') {
            steps { script { run("docker build -t devops-demo:${env.BUILD_NUMBER} -t devops-demo:latest .") } }
        }
        stage('Deploy') {
            steps {
                script {
                    runQuiet('docker rm -f devops-demo')
                    run('docker run -d --name devops-demo -p 5000:5000 devops-demo:latest')
                }
            }
        }
        stage('Verify') {
            steps {
                sleep 5
                script { run('curl -f http://localhost:5000') }
            }
        }
    }
    post {
        success { echo 'Pipeline succeeded' }
        failure { echo 'Pipeline failed' }
    }
}
