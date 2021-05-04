import pandas as pd
import datetime
import pandas_datareader.data as web

def data(arg,kwargs, start, end):

	try:
		df = web.DataReader(arg, kwargs, start, end)
		return df
	except TypeError as e:
		return e
	except NameError as e:
		return e
	except Exception as e:
		return e
	except RemoteDataError as e:
		return e
