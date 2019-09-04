#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- Author: zhaohuan -*-

print([x + y for x in range(0,10) if x%2==0 for y in range(1,100) if y%10==0])