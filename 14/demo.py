#!/usr/bin/env python3
import parser as p

p = p.Parser('titanic.csv')
for r in p.rows:
	print(r.Name)