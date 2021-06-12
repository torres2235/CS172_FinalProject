#!/usr/bin/env bash
echo "Crawling the webs...."
echo ""
cd crawler/
python crawler.py --hops 3 --pages 40
cd ..

echo ""

echo "Indexing documents...."
echo ""
cd indexer/
python indexer.py
cd ..