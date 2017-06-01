var webpack = require('webpack');
var path = require('path');
var loaders = require('./webpack.loaders');
var HtmlWebpackPlugin = require('html-webpack-plugin');
var WebpackCleanupPlugin = require('webpack-cleanup-plugin');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

loaders.push({
  test: /\.scss$/,
  loader: ExtractTextPlugin.extract({fallback: 'style-loader', use : 'css-loader?sourceMap&localIdentName=[local]___[hash:base64:5]!sass-loader?outputStyle=expanded'}),
  exclude: ['node_modules']
});

module.exports = {
  entry: [
    
    'whatwg-fetch',

    //'!!style-loader!css-loader!bootstrap/dist/css/bootstrap.min.css',
    '!!style-loader!css-loader!react-bootstrap-table/dist/react-bootstrap-table-all.min.css',

    //'bootstrap/dist/js/bootstrap.min.js',
    '!!style-loader!css-loader!react-select/dist/react-select.css',

    '!!style-loader!css-loader!react-datepicker/dist/react-datepicker.css',
    '!!style-loader!css-loader!react-datetime/css/react-datetime.css',

    '!!style-loader!css-loader!font-awesome/css/font-awesome.min.css',


    './src/index.jsx',
    './styles/index.scss'

  ],
  output: {
    publicPath: './',		
    path: path.join(__dirname, 'public'),
    filename: 'app.js'
  },
  resolve: {
    extensions: ['.js', '.jsx']
  },
  module: {
    loaders
  },
  plugins: [
    new WebpackCleanupPlugin(),
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: '"production"'
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      compress: {
        warnings: false,
        screw_ie8: true,
        drop_console: true,
        drop_debugger: true
      }
    }),
    new webpack.optimize.OccurrenceOrderPlugin(),
    new ExtractTextPlugin({
      filename: 'style.css',
      allChunks: true
    }),
    new HtmlWebpackPlugin({
      template: './src/template.html',
      files: {
        css: ['style.css'],
        js: ['bundle.js'],
      }
    })
  ]
};
