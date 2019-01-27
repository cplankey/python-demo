node {
   stage('install') {
        withPythonEnv('CPython-2.7'){
            sh 'mkdir package' 
            sh 'cd package'
            sh 'pip install requirements.txt --target /package'
            sh 'cd package'
            sh 'zip -r9 ../function.zip .'
            sh 'cd ../'
            sh 'zip -g function.zip function.py'
        } 
    }
}