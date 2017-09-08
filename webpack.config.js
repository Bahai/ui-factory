var path = require('path');
var webpack = require('webpack');
var HtmlWebpackPlugin = require('html-webpack-plugin');
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
    context: __dirname,
    entry: './app/index.js',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'index_bundle.js'
    },
    module: {
        rules: [
            { test: /\.(js)$/, use: 'babel-loader' },
            { test: /\.css$/, use: [ 'style-loader', 'css-loader' ]}
        ]
    },
    plugins: [
        new BundleTracker({filename: './webpack-stats.json'}),
        new HtmlWebpackPlugin({template: 'app/index.html'})
    ]
}