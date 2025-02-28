
TILE_SIZE = 10

mutable struct Tile
    id::Int
    data::Matrix{Bool}
    neighbours::Array{Int, 1}
    left::Int
    right::Int
    top::Int
    bottom::Int
end

@enum SIDE begin
    NONE=0
    LEFT=1
    RIGHT=2
    TOP=3
    BOTTOM=4
end


function is_neighbour(tile_1::Tile, tile_2::Tile) :: SIDE
    data_1 = tile_1.data
    data_2 = tile_2.data
    edges_1 = Dict([
               (TOP,data_1[1, :])
               (BOTTOM,data_1[end, :])
               (LEFT,data_1[:, 1])
               (RIGHT,data_1[:, end])
              ])
    edges_2 = Dict([
               (TOP,data_2[1, :])
               (BOTTOM,data_2[end, :])
               (LEFT,data_2[:, 1])
               (RIGHT,data_2[:, end])
              ])
    for edge_1 in edges_1, edge_2 in edges_2
        if edge_1.second == edge_2.second || edge_1.second == reverse(edge_2.second)
            return edge_1.first
        end
    end
    return NONE
end

function fill_tileboard!(board::Matrix{Int}, id::Int, position::Tuple{Int, Int}, tiles::Dict{Int, Tile})
    board[position...] = id
    if position == size(board)
        return
    elseif position[2] < size(board)[2]
        new_position = (position[1], position[2]+1)
        new_id = tiles[id].right
    else
        new_position = (position[1]+1, 1)
        new_id = tiles[board[position[1], 1]].bottom
    end
    @assert(new_id != 0, "found id 0 for $(tiles[id]) at $(position)")
    fill_tileboard!(board, new_id, new_position, tiles)
end

function match_tile!(tile::Tile, row::Array{Bool, 1}, side::SIDE)
    @assert(side!=NONE, "No side defined!")
    for _ in 1:2
        for _ in 1:4
            if side == LEFT
                if tile.data[:, 1] == row
                    return
                end
            elseif side  == RIGHT
                if tile.data[:, end] == row
                    return
                end
            elseif side  == TOP
                if tile.data[1, :] == row
                    return
                end
            elseif side  == BOTTOM
                if tile.data[end, :] == row
                    return
                end
            end
            println("rotating $(tile.id)")
            tile.data = rotr90(tile.data)
        end
        println("flipping $(tile.id)")
        tile.data = tile.data[:, end:-1:1]
    end
end

# Demo file has tile arrangement:
# 1951    2311    3079
# 2729    1427    2473
# 2971    1489    1171
#
# Answer calculation:
# 1951 * 3079 * 2971 * 1171 = 20899048083289
function part_1!(tiles::Dict{Int, Tile})
    N = Int(sqrt(length(tiles)))
    tile_board = zeros(Int, 3, 3)
    for (i, entry_1) in enumerate(tiles)
        for (j, entry_2) in enumerate(tiles)
            if j <= i
                continue
            end
            tile_1 = entry_1.second
            tile_2 = entry_2.second
            edge = is_neighbour(tile_1, tile_2)
            if edge == NONE
                continue
            elseif edge == LEFT
                tile_1.left = tile_2.id
                match_tile!(tile_2, tile_1.data[:, end], RIGHT)
                tile_2.right = tile_1.id
            elseif edge == RIGHT
                tile_1.right = tile_2.id
                match_tile!(tile_2, tile_1.data[:, 1], LEFT)
                tile_2.left = tile_1.id
            elseif edge == TOP
                tile_1.top = tile_2.id
                match_tile!(tile_2, tile_1.data[1, :], BOTTOM)
                tile_2.bottom = tile_1.id
            elseif edge == BOTTOM
                tile_1.bottom = tile_2.id
                match_tile!(tile_2, tile_1.data[end, :], TOP)
                tile_2.top = tile_1.id
            end
            push!(tile_1.neighbours, tile_2.id)
            push!(tile_2.neighbours, tile_1.id)
        end
    end
    product = 1
    for entry in tiles
        tile = entry.second
        if length(tile.neighbours) == 2
            product *= tile.id
        end
        if tile.right != 0 &&
           tile.bottom != 0 &&
           tile.left == 0 &&
           tile.top == 0
           fill_tileboard!(tile_board, tile.id, (1,1), tiles)
        end
    end
    println(product)
    display(tile_board)
end

function load_tile_file(file_name:: String) :: Dict{Int, Tile}
    tiles = Dict{Int, Tile}()
    open(file_name) do fid
        data_parsing = false
        row = 1
        id = 0
        data = falses(TILE_SIZE, TILE_SIZE)
        for l in eachline(fid)
            if data_parsing
                data[row, :] = [c == '#' for c in l]
                row += 1
                if row > TILE_SIZE
                    # finished tile push data stop data parsing
                    tiles[id] = Tile(id, data, [], 0, 0, 0, 0)
                    data_parsing = false
                    row = 1
                    data = falses(TILE_SIZE, TILE_SIZE)
                end
            else
                if startswith(l, "Tile")
                    # found tile start data parsing
                    data_parsing = true
                    id = parse(Int,l[6:end-1])
                end
            end
        end
    end
    return tiles
end

function main()
    @assert(length(ARGS) == 1,"Requires one input argument")
    tiles = load_tile_file(ARGS[1])
    tile_count = length(tiles)
    @assert(floor(sqrt(tile_count)) == sqrt(tile_count), "Non square number of tiles loaded $(tile_count)")
    println("loaded $(length(tiles))")
    part_1!(tiles)
end

main()
