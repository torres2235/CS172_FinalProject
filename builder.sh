#!/usr/bin/env bash
echo "Crawling the webs...."
echo ""
cd crawler/
python crawler.py
cd ..

echo ""

echo "Indexing documents...."
echo ""
cd indexer/
python indexer.py
cd ..