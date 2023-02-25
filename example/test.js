const { Worker, isMainThread, parentPort } = require('worker_threads');

if (isMainThread) {
  const worker = new Worker(__filename);

  worker.on('message', (message) => {
    console.log(`Received message from worker: ${message}`);

    worker.terminate();

    // process.exit(1);
  });

  worker.on('exit', () => {
    console.log(`worker exit !!!!!`);
  });

  worker.postMessage('Hello from the main thread!');
} else {
  parentPort.on('message', (message) => {
    console.log(`Received message from main thread: ${message}`);
    parentPort.postMessage('Hello from the worker thread!');

    const boa = require('../'); // @pipcook/boa 

    const testUtils = boa.import('py-src.test-utils');

    testUtils.sum(3, 4, (c) => {
      console.log(`c === ${c}`);
      return `hadfasdfasdf`;
    });

    // Worker.terminate();

    // process.exit(); // 输出完消息后退出程序

  });
}
