# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import time

import grpc

from bolpy.proto import bol_pb2_grpc

from bolpy.evaluator import evaluator

_ONE_DAY_IN_SECONDS = 24 * 60 * 60


class PriceEvaluator(bol_pb2_grpc.PriceEvaluatorServicer):
    def EvaluatePrice(self, request, context):
        print("Evaluating price...")
        e = evaluator.Evaluator(request.historicalPrices)
        return e.evaluate_price(request.currentPrice)


class Server:
    @staticmethod
    def start():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        bol_pb2_grpc.add_PriceEvaluatorServicer_to_server(PriceEvaluator(), server)
        server.add_insecure_port('[::]:50051')
        server.start()

        try:
            while True:
                time.sleep(_ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt:
            server.stop(0)
