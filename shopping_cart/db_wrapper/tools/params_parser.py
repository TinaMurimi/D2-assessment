class ParseParameters:
    @staticmethod
    def parse_insert_params(params):
            params = params._asdict()
            columns = []
            values = ''

            for column, value in params.items():
                if value:
                    columns.append(column)
                    values = values + f", '{value}'"

            _values = values.strip(",").strip()
            _columns = ", ".join(columns)

            return _columns, _values

    @staticmethod
    def parse_update_params(params):
        # try:
        params = params._asdict()
        _params = "{} = '{}'"
        for column, value in params.items():
            if value:
                _params = _params.format(column, value)
                if len(params) == 1:
                    return _params
                else:
                    _update_cols = f"{_params}, {column} = '{value}'"

        return _update_cols

    @staticmethod
    def parse_filters(filters):
        filters = filters._asdict()

        if not filters:
            return ''

        _filters = "WHERE {} = '{}'"
        for column, value in filters.items():
            if value:
                _filters = _filters.format(column, value)
                if len(filters) == 1:
                    return _filters

                next_filter = f"{column} = '{value}'"
                if next_filter not in _filters:
                    _update_cols = f"{_filters} AND {next_filter}"
                else:
                    _update_cols = _filters

                return _update_cols.strip('AND')
