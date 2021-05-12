from deficrawler.protocol_base import ProtocolBase

from datetime import datetime


class Oracle(ProtocolBase):
    def __init__(self, protocol, chain, version):
        super().__init__(
            protocol=protocol,
            chain=chain,
            version=version
        )

    def get_all_pairs(self):

        config = super().get_protocol_config('pair')

        response_data = super().query_data_filtered(
            entity='pair',
            filters=''
        )

        return super().map_data(
            response_data=response_data,
            config=config
        )

    def get_price_from_date_range(self, from_date, to_date, pair):

        from_timestamp = int(
            datetime.strptime(from_date, '%d/%m/%Y %H:%M:%S').strftime("%s"))

        to_timestamp = int(datetime.strptime(
            to_date, '%d/%m/%Y %H:%M:%S').strftime("%s"))

        config = super().get_protocol_config('price')

        pair_name = self.mappings_file['entities']['price']['query']['params']['pair']

        response_data = super().query_data_from_date_range(
            from_timestamp=from_timestamp,
            to_timestamp=to_timestamp,
            entity='price',
            aditional_filters={pair_name: pair}
        )

        return super().map_data(
            response_data=response_data,
            config=config
        )
