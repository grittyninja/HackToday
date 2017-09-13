<?php

namespace app\models;

use Yii;

/**
 * This is the model class for table "users".
 *
 * @property int $id
 * @property string $username
 * @property string $password
 * @property string $role
 */
class UsersDB extends \yii\db\ActiveRecord
{
    /**
     * @inheritdoc
     */
    public static function tableName()
    {
        return 'users';
    }

    /**
     * @inheritdoc
     */
    public function rules()
    {
        return [
            [['username', 'password'], 'required'],
            ['role', 'default', 'value'=>'user'],
            [['username', 'password'], 'string', 'max' => 255, 'min' => 4],
            [['role'], 'string', 'max' => 5],
            ['username', 'checkExist'],
        ];
    }

    /**
     * @inheritdoc
     */
    public function attributeLabels()
    {
        return [
            'id' => 'ID',
            'username' => 'Username',
            'password' => 'Password',
            'role' => 'Role',
        ];
    }

    public function checkExist($attribute, $params){
        $_user = self::find()->where(['username' => $this->username])->one();

        if(count($_user)){
            $this->addError($attribute, 'Username already exist');
        }
    }
}
