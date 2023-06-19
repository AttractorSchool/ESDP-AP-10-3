def get_trd_buy_number_from_lot():
    graphql_query = '''
    query($filter: LotsFiltersInput){
    Lots(filter: $filter)
    {
        trdBuyNumberAnno
    }
}
    '''
