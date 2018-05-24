import tasks


def test_delete_decreases_count(db_with_3_tasks):
    ids = [t.id for t in tasks.list_tasks()]
    # GIVEN 3 items
    assert tasks.count() == 3
    # WHEN we delete one
    tasks.delete(ids[0])
    # THEN count decreases by 1
    assert tasks.count() == 2
