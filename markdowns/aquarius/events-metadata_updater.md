<a name="events.metadata_updater"></a>
# events.metadata\_updater

<a name="events.metadata_updater.MetadataUpdater"></a>
## MetadataUpdater Objects

```python
class MetadataUpdater(BlockProcessingClass)
```

Update price/liquidity info of all known assets.

The update happens in two stages:
1. Initial update is performed if this is ran for the first time. This is determined by
checking for a cached block number from a previous run. The initial update extracts all
Datatoken Ocean balancer pools by looking at the BFactory `BPoolRegistered` event. Then
each Asset in the database is updated with the liquidity/price information from the
corresponding pool.
2. Periodic update is continuously running to detect liquidity updates by looking at the
`LOG_JOIN`, `LOG_EXIT`, and `LOG_SWAP` event logs. The events are detected regardless of
the pool contract, i.e. it looks at all matching events from all BPool contracts or
even any smartcontract event that has the same signature.
See `get_dt_addresses_from_pool_logs`

**Notes**:

  - Set the `BFACTORY_BLOCK` envvar to tell the updater which `fromBlock` to start processing
  events. This should be set to the blockNumber in which the BFactory was created/deployed
  - The continuous updater runs every N seconds (initially set to 20s)
  - The price/liquidity info is added to the Asset's json object under the `price` key, e.g.:
  asset['price'] = {
- `'datatoken'` - 90,
- `'ocean'` - 10,
- `'value'` - 0.111,
- `'type'` - 'pool',
- `'address'` - '0x12112112112...',
- `'pools'` - ['0x12112112112...', ]
  }

