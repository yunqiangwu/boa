

def sum(a, b, fn=None):

    c = a + b
    print(f"{a} + {b} = {c}")

    if fn is not None:
        print(fn(c))

# line_model = None

# 模型预测
# def m_predict(x):
#     global line_model
#     if line_model is None:
#         # 导入 TensorFlow 库并命名为 tf
#         import tensorflow as tf

#         # 创建训练数据；即 x_train 和 y_train
#         x_train = [1, 2, 3, 4]
#         y_train = [0, -1, -2, -3]

#         # 构建模型；使用 tf.keras.Sequential 创建模型
#         line_model = tf.keras.Sequential()
#         # 构建模型；使用 line_model.add 添加一个密集层，该层有 1 个单元并且输入形状为 1
#         line_model.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

#         # 编译模型；line_model.compile 定义优化器、损失函数以及评估指标。
#         line_model.compile(optimizer=tf.keras.optimizers.SGD(0.01), loss='mean_squared_error')

#         # 训练模型；line_model.fit 训练模型，并运行 500 个
#         line_model.fit(x_train, y_train, epochs=50)

#     return line_model.predict([x])[0].tolist()[0]

# 预测结果
# print(line_model.predict([10.0]))

if __name__ == "__main__":
    def cb(c):
        print(f"c = {c}")
    sum(6, 8, cb)
    # print(m_predict(10.0))
    # print(m_predict(15.0))
