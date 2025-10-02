#!/bin/bash

echo "Setting up git hooks..."
git config --local core.hooksPath hooks
chmod +x hooks/*
echo "Hooks activated"
ls -la hooks/
