// vue.config.js
var webpack = require('webpack');
const port = process.env.port || process.env.npm_config_port || 4433
module.exports = {
    publicPath: '/',
    configureWebpack: {
        plugins: [
            new webpack.LoaderOptionsPlugin({
                // test: /\.xxx$/, // may apply this only for some modules
                options: {
                    rules: [
                        {
                            test: /\.s(c|a)ss$/,
                            use: [
                                'vue-style-loader',
                                'css-loader',
                                {
                                    loader: 'sass-loader',
                                    // Requires sass-loader@^7.0.0
                                    options: {
                                        implementation: require('sass'),
                                        fiber: require('fibers'),
                                        indentedSyntax: true // optional
                                    },
                                    // Requires sass-loader@^8.0.0
                                    options: {
                                        implementation: require('sass'),
                                        sassOptions: {
                                            fiber: require('fibers'),
                                            indentedSyntax: true // optional
                                        },
                                    },
                                },
                            ],
                        },
                    ],
                },
            }),
        ],

    },
};
