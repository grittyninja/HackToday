<?php

return [
    'class' => 'yii\db\Connection',
    'dsn' => 'sqlite:'.__DIR__.'/../sqlite/mass.db',
    'username' => '',
    'password' => '',
    'charset' => 'utf8',

    // Schema cache options (for production environment)
    //'enableSchemaCache' => true,
    //'schemaCacheDuration' => 60,
    //'schemaCache' => 'cache',
];
