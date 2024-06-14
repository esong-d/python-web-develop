const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  // lintOnSave: false,
  transpileDependencies: true,
  devServer: {
    host: '127.0.0.1',
    port: 8080,
    open: true,
    proxy: {
      '/user': {
        target: 'http://127.0.0.1:9090',
        ws:false,
        changeOrigin: true,
        pathRewrite: {
          '^/user': ''
        }
      }
    }
  }
})
