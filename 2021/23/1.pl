#!/usr/bin/perl

use Data::Dump;

my @hall;
my @rooms;

my $l=<>;
$l=<>;
$l=<>;
$l=~/\#\#\#(\w)\#(\w)\#(\w)\#(\w)/;
$rooms[0][0]=$1;
$rooms[0][1]=$2;
$rooms[0][2]=$3;
$rooms[0][3]=$4;
$l=<>;
$l=~/\#(\w)\#(\w)\#(\w)\#(\w)/;
$rooms[1][0]=$1;
$rooms[1][1]=$2;
$rooms[1][2]=$3;
$rooms[1][3]=$4;

dd \@rooms;
