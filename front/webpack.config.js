var path = require('path')
var webpack = require('webpack');

module.exports = {
  context: path.resolve(__dirname, './src'),

  entry : {
    app: ['babel-regenerator-runtime','./main.js'],
    vendor: ['react', 'react-dom', 'redux','react-redux','redux-saga']
  },

  output : {
    path: '/home/niburi/dev_cdn/toolStore',
    filename: '[name].js'
  },

  module : {
    rules: [
      {
        test: /\.(js|jsx)$/,
        loader: 'babel-loader',
        exclude: [/node_modules/]
      },

      {
       test: /\.css$/,
       loader: 'style-loader!css-loader?modules'
     },
        {
          test: /\.js$/,
          exclude: [/node_modules/],
          enforce: 'pre',
          use: [{
            loader: 'eslint-loader',
            options: {rules: {semi: 0}}
           }],
         }
        ]}

}
