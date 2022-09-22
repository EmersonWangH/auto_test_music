// 声明式语法包括以下核心流程：
// 1.pipeline : 声明其内容为一个声明式的 pipeline 脚本
// 2.agent: 执行节点（job 运行的 slave 或者 master 节点）
// 3.stages: 阶段集合，包裹所有的阶段（例如：打包，部署等各个阶段）
// 4.stage: 阶段，被 stages 包裹，一个 stages 可以有多个 stage
// 5.steps: 步骤,为每个阶段的最小执行单元,被 stage 包裹
// 6.post: 执行构建后的操作，根据构建结果来执行对应的操作
// ————————————————
pipeline{
    agent any
    stages{
        stage("api_autotest"){
            steps{
                bat 'python main.py'
            }
        }
    }
    post {
    always {
        emailext body: 'test', 
                 subject: 'test report', 
                 to: '12345@qq.com'
    }
    }
}
