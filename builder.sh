#!/usr/bin/env bash
echo "Crawling the webs...."
echo ""
cd crawler/
python3.9 crawler.py
cd ..

echo ""

echo "Indexing documents...."
echo ""
cd indexer/
python3.9 indexer.py
cd ..