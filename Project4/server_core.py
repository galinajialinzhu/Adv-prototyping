@app.route('/other/', methods=['GET'])
def func_result2():
     def genFuncResult2():
            item = pipe_result_rx_queue.get()
            pipe_result_rx_queue.task_done()
            item += bytes('|'.encode('ascii'))
            yield item
return Response(genFuncResult2(), mimetype='application/json; boundary=func_result')**
